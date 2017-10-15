import React, {Component} from 'react'
import moment from 'moment'

class UserBadge extends Component {

  render() {
    const user = this.props.user;
    const created = this.props.created;

    return (
      <div className="pt-card pt-elevation-2 userBadge">
        asked {moment(created).format('ll')}<br/>
        {user.getFullName}
      </div>
    )
  }

}

export default UserBadge