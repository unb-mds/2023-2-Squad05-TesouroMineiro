import logo from '../images/UnB.png';

const Navbar = ({show}) => {

    return (
        <div className={show ? 'sidenav active' : 'sidenav'}>
            <ul>
            
            <img src={logo} alt="Logo" className='logo'/>
            <li>
                <a href="/">Home</a>
                </li>
            <li>
                <a href="/dados">Dados</a>
                </li>
            <li>
                <a href="/sobre">Sobre</a>
                </li>
            <li>
                <a href="/creditos">Créditos</a>
                </li>
            
            </ul>            
        </div>
    )
}

export default Navbar;