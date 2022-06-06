exports.handler = (event, context, callback) => {
  console.log('making call to webhook')
  const url = 'https://api.github.com/repos/Innovation-Information-Initiative/Open-Innovation-Dataset-Index/dispatches';
  const github_PAT = process.env.GH_PAT
  fetch(url, {
    method: "post",
    body: JSON.stringify({
      event_type: 'update_relationship',
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