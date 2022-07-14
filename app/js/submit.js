
	function toggleAddRship() {
		const form = document.getElementById("rship-form");

			if (form.style.display === "block") {
				console.log('block')
				form.style.display = "none";
				document.getElementById('toggleAddRship').innerText = '+';
			} else {
				console.log('none')
				form.style.display = "block";
				document.getElementById('toggleAddRship').innerText = '-';
			}
	}


function handleErrors(response) {
	if (!response.ok) throw new Error(response.status);
	return response;
}


window.onload = function() {
	const form = document.getElementById("rship-form");

	const transform = {
		"parent": "child",
		"child": "parent",
		"similar": "similar",
		"supercedes": "superceded by",
		"superceded by": "supercedes"
	}

	form.addEventListener("submit", function(e) {
		e.preventDefault();
		const data = new FormData(form);
		// const function_url = "https://iiindex.org/.netlify/functions/webhook_trigger"

		const function_url = "http://localhost:4001/.netlify/functions/webhook_trigger"

		const source_uuid = data.get("page-id").split('|')[0]
		const source_shortname = data.get("page-id").split('|')[1]
		const target_uuid = data.get("rship-dataset").split('|')[0]
		const target_shortname = data.get("rship-dataset").split('|')[1]
		const rship_type = data.get("rship-type")
		const inv_rship_type = transform[rship_type]

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

		console.log(rship, inv_rship)
	})
}

