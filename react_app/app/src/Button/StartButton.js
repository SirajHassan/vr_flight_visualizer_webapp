import React from 'react'
import './Button.css'

// ES6
const startButton = (props) => {
  return (
    <div>
      <button onClick={console.log('start')}> Start </button>
    </div>
  	)
}

export default startButton
