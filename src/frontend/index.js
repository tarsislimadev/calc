
const TIME_TO_RESTART = 500;

const pad = (text, length, padding) =>
  text.toString().length < length
    ? pad(padding + text, length, padding)
    : text

const timeOnClock = time => {
  const minutes = Math.floor(time / 60)
  const seconds = time - (minutes * 60)

  return [minutes, seconds]
    .map(time => pad(time, 2, "0"))
    .join(':')
}

function ViewModel() {
  const self = this

  self.level = ko.observable(0)
  self.limit = ko.observable(1000)
  self.gameMessage = ko.observable(null)

  self.numbers = ko.observableArray([])
  self.history = ko.observableArray([])

  self.timeId = null
  self.time = ko.observable(0)
  self.clock = ko.computed(() => timeOnClock(self.time()))

  self.init = () => [self.setNumbers(), self.resetClock()]

  self.startClock = () =>
    self.timeId = setInterval(() => self.time(self.time() + 1), 1000)

  self.stopClock = () =>
    self.timeId !== null
      ? clearInterval(self.timeId)
      : null

  self.resetClock = () => [self.stopClock(), self.time(0), self.startClock()]

  self.setNumbers = () => {
    self.numbers([])

    let i = self.level()
    while (i--) {
      const number = self.createNumber()

      self.numbers.push(number)
      self.numbers.push(number)
    }

    self.numbers.push(self.createNumber())
    self.shuffleNumbers()
  }

  self.createNumber = () => {
    const number = Math.floor(Math.random() * self.limit())

    return self.numbers().indexOf(number) !== -1
      ? self.createNumber()
      : number
  }

  self.shuffleNumbers = () => {
    self.numbers(
      self.numbers().sort(() => {
        return .5 - Math.random()
      })
    )
  }

  self.onNumberClick = number => {
    const numbers = self.numbers().filter(value => value === number)
    self[numbers.length === 1 ? 'won' : 'lose']()
  }

  self.save = won => {
    const history = self.history()
    const time = timeOnClock(self.time())
    history.push({ time, won })
    self.history(history)
  }

  self.levelUp = () => self.level(self.level() + 1)

  self.levelDown = () => self.level(self.level() - 1)

  self.restart = () => setTimeout(() => self.gameMessage(null), TIME_TO_RESTART)

  self.won = () => [self.save(true), self.levelUp(), self.init(), self.restart()]

  self.lose = () => [self.save(false), self.levelDown(), self.init(), self.restart()]
}

$(() => {
  viewModel = new ViewModel()
  ko.applyBindings(viewModel)
  viewModel.init()
})
