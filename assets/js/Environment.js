const {
  Environment,
  Network,
  RecordSource,
  Store,
} = require('relay-runtime');
const store = new Store(new RecordSource());

const network = Network.create((operation, variables) => {
  return fetch('/graphql', {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
    },
    body: JSON.stringify({
      query: operation.text,
      variables,
    }),
  }).then(response => {
    return response.json()
  })
});

const environment = new Environment({
  network,
  store,
});

export default environment