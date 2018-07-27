import React, { Component } from 'react';

class AddProjects extends Component {
    render() {
    
    return (
    <div className="Projects">
        <h3>Add Project</h3>
        <form>
            <div>
                <label>name</label>
                <input type="text" ref ="" />
                <br></br>
                <label>pcb</label>
                <input type="text" ref ="" />
            </div>
        </form>
    </div>
    );
  }
}

export default AddProjects;