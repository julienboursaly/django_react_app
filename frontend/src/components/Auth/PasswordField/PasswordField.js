import React, { useState, useEffect } from 'react';


const initialState = {
	visible : false,
}

const loginField = () => {
	return (
		<input placeholder="password"/>
	);
};

export default loginField