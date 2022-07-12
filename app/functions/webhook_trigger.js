import fetch from 'node-fetch';

exports.handler = (event, context, callback) => {
  console.log('making call to webhook')
  const url = 'https://api.github.com/repos/Innovation-Information-Initiative/Open-Innovation-Dataset-Index/dispatches';
  const github_PAT = process.env.GH_PAT
  const request = JSON.parse(event.body)
  console.log("request is", request.payload)

  fetch(url, {
    method: "post",
    body: JSON.stringify({
      event_type: request.event_type,
      client_payload: request.payload
    }),
    headers: {
      Authorization: "token " + github_PAT,
    },
  })
  .then(handleErrors)
  .then(response => {
    console.log('ok')
    callback(null, {
      statusCode: 200,
      body: 'triggered action'
    })
  })
  .catch((error) => {
    console.error('Error:', error);
    callback(null, {
      statusCode: 502,
      body: 'error with github action'
    })
  });

}

function handleErrors(response) {
    if (!response.ok) throw new Error(response.status);
    return response;
}