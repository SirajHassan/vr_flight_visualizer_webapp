import React, { Component } from 'react'
import './App.css'
import 'aframe'
import 'aframe-particle-system-component'
import { Entity, Scene } from 'aframe-react'
import ReactDOM from 'react-dom'

// nest all components the application might need in this component.

class App extends Component {
  // inherited from Component

  render () {
    return (
      <Scene>
        <Entity geometry={{ primitive: 'box' }} material={{ color: 'red' }} position={{ x: 0, y: 0, z: -5 }} />
        <Entity particle-system={{ preset: 'snow' }} />
        <Entity light={{ type: 'point' }} />
        <Entity gltf-model={{ src: 'virtualcity.gltf' }} />
        <Entity text={{ value: 'Hello, WebVR!' }} />
      </Scene>
    )
  }
}
export default App
