import React, {Component} from 'react'
import QuestionList from './QuestionList'
import Question from './QuestionDetail'
import Navbar from './Navbar'
import {Switch, Route} from 'react-router-dom'

class App extends Component {
  render() {
    return (
      <div>
        <Navbar/>
        <Switch>
          <Route exact path="/" component={QuestionList}/>
          <Route path="/question/:id" component={Question}/>
        </Switch>
      </div>
    )
  }
}

export default App;
