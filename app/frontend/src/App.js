import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios';

import Card from 'react-bootstrap/Card';

function App() {
  const [getMessage, setGetMessage] = useState([])

  const getMessages = async () => {
    const { data } = await axios.get(
      "http://172.22.67.84:5001/"
    );
    const messages = data.data
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
                  { msg['title'] }
              </Card.Title>
              <Card.Subtitle className="text-muted" style={{ fontSize: '.75em', margin: '10px 0px' }}>
                { msg['keywords'] }
              </Card.Subtitle>
              <Card.Text style={{ color: "black", fontSize: '.75em' }}>
                { msg['summary'] }
              </Card.Text>
              <Card.Link href={ msg['link']} style={{ fontSize: '.75em' }} target='_blank'>
                { msg['link']}
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
