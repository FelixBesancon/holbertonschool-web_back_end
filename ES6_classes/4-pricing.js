import Currency from "./3-currency.js";

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
  }

  get amount() {
    return this._amount
  }

  get currency() {
    return this._currency
  }

  set amount(amount) {
    if (typeof amount !== 'number') {
      throw new TypeError ('Amount must be a number');
    }
    this._amount = amount;
  }

  set currency(currency) {
    if (!(currency instanceof Currency)) {
      throw new TypeError ('Currency must be an instance of Currency');
    }
    this._currency = currency;
  }

  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number') {
      throw new TypeError ('Amount must be a number');
    }
    if (typeof conversionRate !== 'number') {
      throw new TypeError ('ConversionRate must be a number');
    }
    return amount * conversionRate;
  }
}
