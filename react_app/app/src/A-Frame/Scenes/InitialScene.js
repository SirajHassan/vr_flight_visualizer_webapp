import React, { Component } from 'react'
import 'aframe'
import { Entity, Scene } from 'aframe-react'

class InitialScene extends Component {
  render () {
	    return (
        <div>
            <Scene>
              <Entity geometry={{ primitive: 'box' }} material={{ color: 'red' }} position={{ x: 0, y: 0, z: -5 }} />
              <Entity light={{ type: 'point' }} />
              <Entity gltf-model={{ src: 'virtualcity.gltf' }} />
              <Entity text={{ value: 'Welcome!' }} />
            </Scene>
        </div>
	    )
  }
}

export default InitialScene
