import React, { Component } from 'react';
import Projects from './Components/Projects'
import AddProject from './Components/AddProject'
import './App.css';

class App extends Component {
  constructor() {
    super();
    this.state = {
      projects:[]
    }
  }

  componentWillMount(){
    this.setState({projects: [
    { 
      name: 'Boston',
      pct: '646'
    },
    {
      name: 'Atlanta',
      pct: '543'
    },
    {
      name: 'Washington',
      pct: '435'
    }
    ]});
  }
  render() {
    return (
      <div className="App">
        <AddProject />
        <Projects projects = {this.state.projects} />
      </div>
    );
  }
}

export default App;
