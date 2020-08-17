import React, { Component } from 'react'
import Form from '../Form/Form'
import StartButton from '../Button/StartButton'
import PauseButton from '../Button/PauseButton'

// nest all components the application might need in this component.

class ControlPanel2D extends Component {
  // inherited from Component

  render () {
    return (
      <div className='ControlPanel2D'>
        <Form />
        <StartButton />
        <PauseButton />
      </div>
    )
  }
}
export default ControlPanel2D
