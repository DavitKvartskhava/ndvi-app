import React from "react";
import "./App.css";
import ImageWindow from "./components/ImageWindow";
import FilenameForm from "./components/FilenameForm";
import "bootstrap/dist/css/bootstrap.min.css";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { filename: null, loadedImages: false };
  }

  updateFilename = (newFilename) => {
    this.setState({ filename: newFilename, loadedImages: false });
  };

  loadingFinishedUpdate = () => {
    this.setState({ loadedImages: true });
  };

  render() {
    return (
      <div className="App">
        <h1 style={{ marginBottom: "30px" }}>Image analysis</h1>
        <h3 style={{ marginBottom: "30px" }}>
          Please provide the filename below
        </h3>
        <FilenameForm updateFilename={this.updateFilename} />
        {this.state.filename ? (
          <Container fluid>
            <Row>
              <Col md={6}>
                <ImageWindow
                  analysisType="NIRI"
                  reqURL="http://127.0.0.1:5000/nir?filename="
                  filename={this.state.filename}
                  loaded={this.state.loadedImages}
                  loadingHandler={this.loadingFinishedUpdate}
                />
              </Col>
              <Col md={6}>
                <ImageWindow
                  analysisType="NDVI"
                  reqURL="http://127.0.0.1:5000/ndvi?filename="
                  filename={this.state.filename}
                  loaded={this.state.loadedImages}
                  loadingHandler={this.loadingFinishedUpdate}
                />
              </Col>

              <Col md={6}>
              <ImageWindow
                  analysisType="VARI"
                  reqURL="http://127.0.0.1:5000/vari?filename="
                  filename={this.state.filename}
                  loaded={this.state.loadedImages}
                  loadingHandler={this.loadingFinishedUpdate}
                />
              </Col>

              <Col md={6}>
              <ImageWindow
                  analysisType="TGI"
                  reqURL="http://127.0.0.1:5000/tgi?filename="
                  filename={this.state.filename}
                  loaded={this.state.loadedImages}
                  loadingHandler={this.loadingFinishedUpdate}
                />
              </Col>
            </Row>
          </Container>
        ) : (
          <></>
        )}
      </div>
    );
  }
}

export default App;
