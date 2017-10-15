import React, {Component} from 'react'

class Navbar extends Component {

  render() {
    const authElement = user.isAuthenticated ? user.fullName :
      (<a href="/login">Log In</a>);
    return (
      <nav className="pt-navbar pt-fixed-top .modifier">
        <div className="pt-navbar-group pt-align-left">
          <div className="pt-navbar-heading">DoubleFault</div>
          <input className="pt-input" placeholder="Search questions..." type="text"/>
        </div>
        <div className="pt-navbar-group pt-align-right">
          <button className="pt-button pt-minimal pt-icon-user">
            {authElement}
          </button>
          <button className="pt-button pt-minimal pt-icon-cog"></button>
        </div>
      </nav>
    )
  }
}

export default Navbar
