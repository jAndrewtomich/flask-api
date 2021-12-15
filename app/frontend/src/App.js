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
    // console.log(data.text)
  };

  useEffect(()=>{
    getMessages();
  }, []);


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          React + Flask Tutorial
        </p>
        <div style={{ maxWidth: '100%', textAlign: 'left'}}>
          {getMessage.map((message) => (
            <Card key={message[0].key}>
              <Card.Body>
                <Card.Title ><h1 style={{ color: 'black' }}>{ message[1].heading }</h1></Card.Title>
                <Card.Subtitle className="text-muted" style={{ margin: '0px 100px 0px 100px'}}>{ message[3].keywords }</Card.Subtitle>
                <Card.Text style={{ color: 'black' }}>
                  { message[2].summary }
                </Card.Text>
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
