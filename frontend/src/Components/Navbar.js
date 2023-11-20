import logo from '../images/UnB.png';

const Navbar = ({ show }) => {

    return (
        <div style={{ width: '130px' }} className={show ? 'sidenav active' : 'sidenav'}>
            <ul className='d-flex flex-column mx-0'>
                <li>
                    <img src={logo} alt="Logo" className='logo ms-3' />
                </li>

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