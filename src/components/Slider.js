import React from "react";

class Slider extends React.Component {
  constructor(props) {
    super(props);
  }

  handleChange = (e) => {
    let value = parseInt(e.target.value);
    this.props.onChange(this.props.type, value);
  };

  render() {
    return (
      <div>
        <label>
          {this.props.type}
          <br />
          <input
            type="range"
            min="1"
            max="200"
            value={this.props.value}
            onChange={this.handleChange}
          />
          <br />
        </label>
      </div>
    );
  }
}

export default Slider;
