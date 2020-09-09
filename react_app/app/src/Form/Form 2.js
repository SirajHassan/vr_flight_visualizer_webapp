import React, { Component } from 'react'
import NumericInput from 'react-numeric-input'
class Form extends Component {
  render () {
	  return (
  	  	<div>
        <p> Latitude: </p>
        <NumericInput step={1} precision={4} value={0.0} min={-90} max={90} />
        <p> Longitude </p>
        <NumericInput step={1} precision={4} value={0.0} min={-180} max={180} />
  	  	</div>
    )
  }
}

export default Form
