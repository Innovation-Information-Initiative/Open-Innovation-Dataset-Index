const fetch = require('node-fetch')

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
  });

  // mod this to run differently on success/failure
  callback(null, {
    statusCode: 200,
    body: 'made post req'
  })
}