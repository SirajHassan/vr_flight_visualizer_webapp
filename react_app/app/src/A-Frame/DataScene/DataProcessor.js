
import React, { Component } from 'react'
import 'aframe'
import { Entity, Scene } from 'aframe-react'
import axios from 'axios'
import DataDisplay from './DataDisplay'

class DataProcessor extends Component {

  state = {
    api_data: []
  }

  // parseTuple(t) {
  //   t= t.toString();
  //   return JSON.parse("[" + t.replace(/\(/g, "[").replace(/\)/g, "]") + "]");
  // }

  organizeData(res) {
    var api_data = [];
    for(var i = 0; i < res.data.states.length; i++){
      api_data.push(res.data.states[i][17]);
    }
    this.setState({ api_data });

  }



  componentDidMount() {
    this.interval = setInterval(() =>

        axios.get(`https://uzqalcxe2f.execute-api.us-east-1.amazonaws.com/test1/flights?lat=46.2044&lon=6.1432&radius=200`)
          .then(res => {
            // const api_data = res.data.states[0];
            // this.setState({ api_data });
            this.organizeData(res);
            console.log(this.api_data)
          })
          .catch(error => console.log(error))
        ,5000);
  }

  componentWillUnmount(){
    clearInterval(this.interval);
  }

  render () {
	    return (
        <div>
            <p>{this.state.api_data[0][0]}</p>

            <Scene>
              <Entity geometry={{ primitive: 'box' }} material={{ color: 'red' }} position={{ x: 0, y: 0, z: -5 }} />
              <Entity light={{ type: 'point' }} />
            </Scene>
        </div>
	    )
  }
}

export default DataProcessor
