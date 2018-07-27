import React, { Component } from 'react';

class ProjectItem extends Component {
  render() {
    // console.log(this.props);
    return (
      <li className="Projects">
        <strong>{this.props.project.name} </strong> : {this.props.project.pct}
      </li>
    );
  }
}

export default ProjectItem;