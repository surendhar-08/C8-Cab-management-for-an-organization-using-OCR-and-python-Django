import React, { useEffect, useState } from 'react'

function dateConvert(da) {

	const d = new Date(da)
	const y = d.getFullYear()
	const m = d.getMonth() + 1
	const dat = d.getDate()
	return dat + '-' + m + '-' + y

}

function timeConvert(da) {

	const d = new Date(da)
	var h = d.getHours()
	var m = d.getMinutes()
	if (h < 10) {
		h = "0" + h
	}
	return h + ':' + m

}

function JsonDataDisplay() {

	const [JsonData, setJsonData] = useState([])

	useEffect(() => {

		const interval = setInterval(() => {
			fetchData()
		}, 5000)

		const url = "http://127.0.0.1:8000/cars/?format=json"
		const fetchData = async () => {
			try {
				const response = await fetch(url)
				const json = await response.json()
				setJsonData(json)
			} catch (error) {
				console.log("error", error)
			}
		};

		return () => clearInterval(interval)
	}, [])

	const DisplayData = JsonData.map(

		(info) => {
			return (
				<tr>
					<td>{info.id}</td>
					<td>{info.number_plate}</td>
					<td>{dateConvert(info.enter_date)}</td>
					<td>{timeConvert(info.enter_date)}</td>
				</tr>
			)
		}
	)


	return (
		<div className="container">
			<div className="row">
				<div className="col-12">
					<div className="card">
						<div className="card-body text-center">
							<h3 className="card-title m-b-0">LIST OF CARS</h3>
						</div>
						<div className="table-responsive">
							<table className="table" id="c">
								<thead className="thead-light">
									<tr>
										<th scope="col">ID</th>
										<th scope="col">Number Plate</th>
										<th scope="col">Date</th>
										<th scope="col">Time</th>
									</tr>
								</thead>
								<tbody className="customtable">
									{DisplayData}
								</tbody>
							</table>
						</div>
					</div>
				</div>
			</div>
		</div>
	)
}

export default JsonDataDisplay;