import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios';

import Card from 'react-bootstrap/Card';

function App() {
  const [getMessage, setGetMessage] = useState([])

  const getMessages = async () => {
    const { data } = await axios.get(
      "http://127.0.0.1:5000/flask/endpoint"
    );
    const messages = data.text
    setGetMessage(messages);
    // console.log(messages)
    // console.log(data.text)
  };

    useEffect(()=>{
      getMessages();
    }, []);

  function Summary({ msgs }) {
    return (
      <div className="container">
      {/* { console.log(getMessage) } */}
        { getMessage.map(msg => (
          <Card key={ msg.id }>
            <Card.Body>
              <Card.Title>{ msg.split(" ").slice(0, 5) }</Card.Title>
              <Card.Subtitle className="text-muted">{ msg.keywords }</Card.Subtitle>
              <Card.Text>
                { msg.summary }
              </Card.Text>
            </Card.Body>
          </Card>
        ))}
      </div>
    );
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          React + Flask Tutorial
        </p>
        { console.log(getMessage) }
        { /*<Summary
          items = { getMessage }
        /> */}
        <div className="container">
        { getMessage.map(msg => (
          <Card key={ msg.id }>
            <Card.Body>
              <Card.Title style={{ color: "black", fontSize: '1.5em' }}>{ msg.split("Title :")[1].split("Summary :")[0] }</Card.Title>
              <Card.Subtitle className="text-muted" style={{ fontSize: '1em'}}>{ msg.split("*<>*")[2] }</Card.Subtitle>
              <Card.Text style={{ color: "black" }}>
                { msg.split("*<>*")[1] }
              </Card.Text>
              <Card.Link href={ msg.split("*<>*")[3]}>{ msg.split("*<>*")[3]}</Card.Link>
            </Card.Body>
          </Card>
        ))}
      </div> 
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
