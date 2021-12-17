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
  };

  useEffect(()=>{
    getMessages();
  }, []);

  const Summary = () => {
    return (
        getMessage.map((msg, index) => (
          <Card key={ index } style={{ border: '10px', borderStyle: 'solid', borderColor: '#d1d1e0', margin: '20px 0px', textAlign: 'justify'  }}>
            <Card.Body>
              <Card.Title style={{ color: "black", fontSize: '1.25em' }}>
                  { msg.split("*<>*")[0] }
              </Card.Title>
              <Card.Subtitle className="text-muted" style={{ fontSize: '.75em', margin: '10px 0px' }}>
                { msg.split("*<>*")[2] }
              </Card.Subtitle>
              <Card.Text style={{ color: "black", fontSize: '.75em' }}>
                { msg.split("*<>*")[1] }
              </Card.Text>
              <Card.Link href={ msg.split("*<>*")[3]} style={{ fontSize: '.75em' }} target='_blank'>
                { msg.split("*<>*")[3]}
              </Card.Link>
            </Card.Body>
          </Card>
        ))
    );
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1 style={{ fontSize: '2em' }}>
         ANDREW'S NEWS AGGREGATION 
        </h1>
        <div className="container-fluid" style={{ maxWidth: '80%'}}>
          <Summary/>
        </div>
      </header>
    </div>
  );
}

export default App;
