import React, { Component } from 'react';
import axios from 'axios';

class Gs extends Component {
  state = {
    gsResult: '',
    coeffHistory: '',
    history: '',
    a: '',
    k: '',
    n: ''
  };
d
  // componentDidMount() {
  //   this.fetchValues();
  //   this.fetchIndexes();
  // }

  async fetchGs() {
    const values = await axios.get(
      `http://127.0.0.1:5555/gs_cal/?a=${this.state.a}&k=${this.state.k}&n=${this.state.n}`
      );
    this.setState({ gsResult: values.data });
  }

  async fetchHistory() {
    const resultHistory = await axios.get('http://127.0.0.1:5555/gs_cal/history');
    this.setState({
      history: resultHistory.data,
    });
  }

    async fetchCoeff() {
    const coeffHistory = await axios.get('http://127.0.0.1:5555/gs_cal/history/coefficients');
    this.setState({
      coeffHistory: coeffHistory.data.result.map(coefficient => <p>coefficient: {coefficient.coefficient}</p>)
    });
  }

  handleSubmitGs = async (event) => {
    event.preventDefault();

    this.fetchGs();
    this.setState({ a: '' , k: '', n: ''});
  };

  handleSubmitHistory = async (event) => {
    event.preventDefault();

    this.fetchHistory();
  };


  handleSubmitCoeff = async (event) => {
    event.preventDefault();

    this.fetchCoeff();
  };


  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmitGs}>
          <label>Enter firstElem, coefficient, and number:</label><br />
          <input
            value={this.state.a}
            onChange={(event) => this.setState({ a: event.target.value })}
          /><br />
          <input
            value={this.state.k}
            onChange={(event) => this.setState({ k: event.target.value })}
          /><br />
          <input
            value={this.state.n}
            onChange={(event) => this.setState({ n: event.target.value })}
          />
          <br />
          <button>Calculate</button>
        </form>
        <h3>
          GS result:
        </h3>
        {JSON.stringify(this.state.gsResult.result)}

        <br /><br />

        <form onSubmit={this.handleSubmitHistory}>
          <button>Show last five calculating</button>
        </form>

        <h3>
          History:
        </h3>
        {JSON.stringify(this.state.history)}
        <br /> <br />

        <form onSubmit={this.handleSubmitCoeff}>
          <button>Show last five coefficients</button>
        </form>

        <h3>
          Coefficients:
        </h3>
        {this.state.coeffHistory}
        <br />

        {/* <h3>Indexes I have seen:</h3>
        {this.renderSeenIndexes()}

        <h3>Calculated Values:</h3>
        {this.renderValues()} */}
      </div>
    );
  }
}

export default Gs;
