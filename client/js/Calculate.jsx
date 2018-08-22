import React from "react";
import {Row, Col, Button, Input, InputGroup, FormGroup} from 'reactstrap';
import {AvForm, AvField} from 'availity-reactstrap-validation';
import _debounce from 'lodash.debounce';
import axios from 'axios';

export default class CalculateForm extends React.Component {
  constructor(props) {
    super(props);

    this.handleValidSubmit = this.handleValidSubmit.bind(this);
    this.state = {
      vector1: false,
      vector2: false,
      result: 'Result will appear here'
    }
  }

  handleValidSubmit(event, values) {
    this.setState({values});

    let vector1_array = values.vector1.split(',');
    let vector2_array = values.vector2.split(',');

    vector1_array = vector1_array.map(Number);
    vector2_array = vector2_array.map(Number);

    axios.post('http://' + process.env.API_HOST + ':5000/calculate', {
      vector1: vector1_array,
      vector2: vector2_array
    })
      .then((response) => {
        this.setState({result: response.data.result})
      })
      .catch((error) => {
        console.log(error);
      });
  }

  checkFormat = (array) => {
    const result = array.every(function (item) {
      return !isNaN(item);
    });
    return result;
  };

  validate = _debounce((value, ctx, input, cb) => {

    let raw_array = value.split(',');

    if (raw_array.length !== 3) {
      return false;
    }

    let clean_array = raw_array.map(c => c.trim());
    cb(this.checkFormat(clean_array));
  }, 200);

  render() {
    return (
      <div>
        <AvForm onValidSubmit={this.handleValidSubmit}>
          <Row>
            <Col sm={{size: 'auto', offset: 2}}>
              <AvField label="Vector 1" value={this.state.vector1} type="text" name="vector1" id="vector1"
                       placeholder="1, 2, 3"
                       validate={{async: this.validate}} required/>
            </Col>
            <Col sm={{size: 'auto', offset: 2}}>
              <AvField label="Vector 2" value={this.state.vector2} type="text" name="vector2" id="vector2"
                       placeholder="4, 5, 6"
                       validate={{async: this.validate}} required/>
            </Col>
          </Row>
          <Row className="center mt-2">
            <Col></Col>
            <Col>
              <InputGroup className="center">
                <Input placeholder="Result" value={this.state.result} readOnly/>
              </InputGroup>
            </Col>
            <Col></Col>
          </Row>
          <div className="text-center">
            <FormGroup>
              <Button style={{margin: '10px'}} color="primary">Submit</Button>
            </FormGroup>
          </div>
        </AvForm>
      </div>
    );
  }
}
