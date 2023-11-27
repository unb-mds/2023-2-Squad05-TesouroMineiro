import React, { useState, useRef, useEffect } from 'react';
import Chart from 'react-apexcharts';
import credsup from '../../Analises/CredSup.json'

const Graficos = () => {
  const [selectedMunicipio, setSelectedMunicipio] = useState();
  const [selectedData, setSelectedData] = useState('30');
  const chartRef = useRef(null);

  const [municipios, setMunicipios] = useState([]);
  const [chartData, setChartData] = useState([]);
  const [series, setSeries] = useState([]);

  useEffect(() => {
    let newarr = []
    credsup.forEach((d)=>{
      newarr.push(d.Municipio)
    })
    setMunicipios([...newarr])
  },[])

  const handleMunicipioChange = (e) => {
    setSelectedMunicipio(e.target.value);
    let series = []
    let data = []
    credsup.forEach((d) => {
      if(d.Municipio === e.target.value){
        d.Analises.forEach((a) => {
          console.log("A")
          console.log(a)
          series.push(a.Soma)
          data.push(a.Data)
        })
      }
    })
    setChartData([...data])
    console.log(chartData)
    setSeries([...series])
    console.log(series)
  };

  const handleDataChange = (e) => {
    setSelectedData(e.target.value);
  };

  const dataExample = {
    options: {
      chart: {
        id: 'example',
      },
      xaxis: {
        categories: chartData,
      },
    },
    series: [
      {
        name: '',
        data: series,
      },
    ],
  };



  return (
    <div
      className=''
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        
      }}
    >
      <div className='d-flex flex-column my-3 w-75 justify-content-center' style={{ marginBottom: '20px', width: '350px' }}>
        <div className='d-flex mb-2' style={{height:'70px'}}>
          <label className='input-group-text' onClick={() => {
            console.log(chartData)
            console.log(series)
          }} >
            Município:
          </label>
          <select className='form-select' value={selectedMunicipio} onChange={(e)=> handleMunicipioChange(e)}>
            {municipios.map((municipio) => (
              <option key={municipio} value={municipio}>
                {municipio}
              </option>
            ))}
          </select>
        </div>
        <div className='d-flex' style={{height:'70px'}}>
          <label className='input-group-text'>
            Categoria:
          </label>
          <select className='form-select' value={selectedData} onChange={handleDataChange}>
            
              <option value>
                Crédito Suplementar
              </option>
            
          </select>
        </div>
      </div>
      <div className='mt-5 mb-5 grafico'>
        <Chart
          options={dataExample.options}
          series={dataExample.series}
          type="bar"
          
          ref={chartRef}
        />
      </div>
    </div>
  );
};

export default Graficos;
