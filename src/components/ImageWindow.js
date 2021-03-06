import React from "react";
import Slider from "./Slider";

class ImageWindow extends React.Component {
  constructor(props) {
    super(props);
    this.state = { brightness: 100, contrast: 100, saturation: 100, sepia: 0};
  }

  updateState = (setting, range) => {
    this.setState({ ...this.state, [setting]: range });
  };

  render() {
    console.log(this.state);
    return (
      <div className="window" style={{marginBottom: '70px', padding: "20px 20px 20px 20px"}}>
        <h1>{this.props.analysisType}</h1>
        <img
          src={(this.props.loaded) ? this.props.reqURL + this.props.filename : "/loading.gif"}
          style={{
            filter: `brightness(${this.state.brightness}%) 
                    contrast(${this.state.contrast}%) 
                    saturate(${this.state.saturation}%)
                    sepia(${this.state.sepia}%)`

          }}
          onLoad={() => {this.props.loadingHandler()}}
          width="100%"
          height="auto"
          alt="niri_img"
        />

        <Slider
          type="brightness"
          value={this.state.brightness}
          onChange={this.updateState}
        />
        <Slider
          type="contrast"
          value={this.state.contrast}
          onChange={this.updateState}
        />
        <Slider
          type="saturation"
          value={this.state.sharpness}
          onChange={this.updateState}
        />
        <Slider
          type="sepia"
          value={this.state.sepia}
          onChange={this.updateState}
        />
      </div>
    );
  }
}

export default ImageWindow;
