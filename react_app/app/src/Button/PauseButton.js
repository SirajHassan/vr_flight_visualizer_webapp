import React from 'react'
import './Button.css'

// ES6
const pauseButton = (props) => {
  return (
    <div>
      <button onClick={console.log('pause')}> Pause </button>
    </div>
  	)
}

export default pauseButton
