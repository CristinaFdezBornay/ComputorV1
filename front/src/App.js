import React, { useState } from 'react';
import './App.css';

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  const handlePostQuery = async () => {
    const data = {
      rawEquation: '-98 * X^0 -2.6 * X^1 -3.1 * X^2 = -4 * x^0 -23 * X^1 -3.1 * X^2 ',
    }
    const requestOptions = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': 'Content-Type',
      },
      mode: 'cors',
      body: JSON.stringify(data)
    }
    await fetch('http://localhost:5000/api/', requestOptions)
    .then( async(responsePetition)  => {
      const response = await responsePetition.json()
      setCurrentTime(response.time)
      console.log(response)
    })
    .catch( error => {
        console.log(error);
    });
}

  return (
    <div className='App'>
      <header className='App-header'>

        <button
          onClick={handlePostQuery}
        >Hello lol</button>
        <br/>
        ... no changes in this part ...
        <p>The current time is {currentTime}.</p>
      </header>
    </div>
  );
}

export default App;
