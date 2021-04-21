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
    this.state = { filename: null };
  }

  updateFilename = (newFilename) => {
    this.setState({ filename: newFilename });
  };

  render() {
    return (
      <div className="App">
        <h1 style={{ marginBottom: "30px" }}>Image analysis</h1>
        <FilenameForm updateFilename={this.updateFilename} />

        <Container fluid>
          <Row>
            <Col md={6}>
              <ImageWindow
                analysisType="NIRI"
                reqURL="http://127.0.0.1:5000/nir?filename="
                filename={this.state.filename}
              />
            </Col>
            <Col md={6}>
              <ImageWindow
                analysisType="NDVI"
                reqURL="http://127.0.0.1:5000/ndvi?filename="
                filename={this.state.filename}
              />
            </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

export default App;
