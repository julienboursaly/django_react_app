import React, { Component, useState, useEffect } from 'react';
import axios from 'axios';

import DummyData from './../DummyData/DummyData';


const initialState = {
	data : [],
}

const fullData = () => {
	const [state, setState] = useState(initialState);

	useEffect(() => {
			axios
				.get('http://localhost:8000/api/dummy/')
				.then(result => setState({ ...state, data: result.data }))
				.catch(error => console.log(error));
		}, []);

	const data = state.data.map((dummyData, key) => (
			<DummyData name={ dummyData.name } data={ dummyData.data} key={ key }/>
		));
	
	return (
		<div>{ data }</div>
	);
};

//class FullData extends Component {
//	state = initialState;
//
//	componentDidMount () {
//		axios
//			.get('http://localhost:8000/api/dummy/')
//			.then(result => this.setState({ data:result.data }))
//			.catch(error => console.log(error));
//	}
//
//	render() {
//		const data = this.state.data.map((dummyData, key) => {
//			return (
//				<DummyData name={ dummyData.name } data={ dummyData.data} key={ key }/>
//			);
//		});
//
//		return (
//			<div>{ data }</div>
//		);
//	}
//}

export default fullData