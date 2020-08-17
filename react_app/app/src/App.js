import React, { Component } from 'react'
import './App.css'
import 'aframe'
import { Entity, Scene } from 'aframe-react'
import ReactDOM from 'react-dom'
import ControlPanel2D from './Control-panel/ControlPanel2D'
import InitialScene from './A-Frame/Scenes/InitialScene'

// nest all components the application might need in this component.

class App extends Component {
  // inherited from Component

  render () {
    return (
      <div className='App'>
        <InitialScene />
        <ControlPanel2D />
      </div>
    )
  }
}
export default App
