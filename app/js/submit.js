function toggleAddRship() {
	console.log('toggling')
	const form = $("#rship-form");
	form.toggle();
	if (form.is(':visible')) {
		$('#toggleAddRship').text('-');
	} else {
		$('#toggleAddRship').text('+');
	}
}


function handleErrors(response) {
	if (!response.ok) throw new Error(response.status);
	return response;
}


window.onload = function() {
	const form = $("#rship-form");

	const transform = {
		"parent": "child",
		"child": "parent",
		"similar": "similar",
		"supercedes": "superceded by",
		"superceded by": "supercedes"
	}

	form.on("submit", function(e) {
		e.preventDefault();
		const data = new FormData(form[0]);
		// const function_url = "https://iiindex.org/.netlify/functions/webhook_trigger"

		const function_url = "http://localhost:4001/.netlify/functions/webhook_trigger"

		const source_uuid = data.get("pageId").split('|')[0]
		const source_shortname = data.get("pageId").split('|')[1]
		const target_uuid = data.get("rshipDataset").split('|')[0]
		const target_shortname = data.get("rshipDataset").split('|')[1]
		const rship_type = data.get("rshipType")
		const inv_rship_type = transform[rship_type]

		if (source_uuid !== target_uuid){

			const rship = {
				"uuid": target_uuid,
				"shortname": target_shortname,
				"relationship_type": rship_type
			}


			fetch(function_url, {
				method: "post",
				body: JSON.stringify({
					event_type: 'update_relationship',
					payload: {
						rship: rship,
						uuid: source_uuid
					}
				})
			})
			.then(handleErrors)
			.then(response => {
				alert("Success! Thanks for adding a new relationship. It will take about a minute for the site to update with the new addition.")
				form[0].reset();
				console.log(response.status)
			})
			.catch((error) => {
				console.error('Error:', error);
			});

			//inverse relationship
			const inv_rship = {
				'uuid': source_uuid,
				'shortname': source_shortname,
				'relationship_type': inv_rship_type
			}

			fetch(function_url, {
				method: "post",
				body: JSON.stringify({
					event_type: 'update_relationship',
					payload: {
						rship: inv_rship,
						uuid: target_uuid
					}
				})
			})
			.then(handleErrors)
			.then(response => {
				console.log(response.status)
			})
			.catch((error) => {
				console.error('Error:', error);
			});
		}

		else {
			alert("Target dataset can't match source!")
		}

	})
}

