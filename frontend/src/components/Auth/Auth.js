import React, { useState, useEffect } from 'react';

import LoginField from './LoginField/LoginField';
import PasswordField from './LoginField/PasswordField';


const auth = () => {
	return (
		<div>
			<LoginField/>
			<PasswordField/>
		</div>
	);
};

export default auth