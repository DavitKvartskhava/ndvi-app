import React from "react";

class FilenameForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = { value: "", lastValue: "" };
  }
  handleChange = (event) => {
    this.setState({ value: event.target.value });
  };

  handleSubmit = (event) => {
    this.props.updateFilename(this.state.value);
    this.setState({ value: "", lastValue: this.state.value });
    event.preventDefault();
  };

  render() {
    return (
      <>
        <form onSubmit={this.handleSubmit}>
          <label>
            Filename:
            <input
              type="text"
              value={this.state.value}
              onChange={this.handleChange}
            />
          </label>
          <input type="submit" />
        </form>

        <h3 style={{ textAlign: "center", marginTop: "50px" }}>
          Analyzing file:
          {this.state.lastValue}
        </h3>
      </>
    );
  }
}

export default FilenameForm;
