// App.jsx
import React from "react";
import {Jumbotron, Container, Row, Col} from 'reactstrap';
import CalculateForm from './Calculate';

export default class App extends React.Component {
  render() {
    return (
      <Container>
        <Jumbotron className={"text-center"}>
          <h1>Welcome to Kyle's Super Simple Cross Product Calculator</h1>
          <p>
            Simply input two different vectors into the shown form fields to calculate their cross product!
          </p>
        </Jumbotron>
        < CalculateForm/>
      </Container>);
  }
}