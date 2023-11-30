import React, { useState, useRef, useEffect } from 'react';
import Chart from 'react-apexcharts';
import credsup from '../../Analises/CredSup.json';

const Graficos = () => {
  const [selectedMunicipio, setSelectedMunicipio] = useState();
  const [selectedData, setSelectedData] = useState('30');
  const [reportType, setReportType] = useState('geral');
  const chartRef = useRef(null);

  const [municipios, setMunicipios] = useState([]);
  const [chartData, setChartData] = useState([]);
  const [series, setSeries] = useState([]);

  useEffect(() => {
    let newarr = [];
    credsup.forEach((d) => {
      newarr.push(d.Municipio);
    });
    setMunicipios([...newarr]);
  }, []);

  const handleMunicipioChange = (e) => {
    setSelectedMunicipio(e.target.value);
    fetchChartData(e.target.value, selectedData, reportType);
  };

  const handleDataChange = (e) => {
    setSelectedData(e.target.value);
    fetchChartData(selectedMunicipio, e.target.value, reportType);
  };

  const handleReportTypeChange = (e) => {
    setReportType(e.target.value);
    fetchChartData(selectedMunicipio, selectedData, e.target.value);
  };

  const fetchChartData = (selectedMunicipio, selectedData, reportType) => {
    let series = [];
    let data = [];

    credsup.forEach((d) => {
      if (d.Municipio === selectedMunicipio) {
        d.Analises.forEach((a) => {
          if ((reportType === 'geral') || // Adiciona condição para relatório geral
              (reportType === 'anual' && a.Data.includes(selectedData.slice(0, 4)))) {
            series.push(a.Soma);
            data.push(a.Data);
          }
        });
      }
    });

    setChartData([...data]);
    setSeries([...series]);
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
        <div className='d-flex mb-2' style={{ height: '70px' }}>
          <label className='input-group-text'>
            Município:
          </label>
          <select className='form-select' value={selectedMunicipio} onChange={(e) => handleMunicipioChange(e)}>
            {municipios.map((municipio) => (
              <option key={municipio} value={municipio}>
                {municipio}
              </option>
            ))}
          </select>
        </div>
        <div className='d-flex mb-2' style={{ height: '70px' }}>
          <label className='input-group-text'>
            Categoria:
          </label>
          <select className='form-select' value={selectedData} onChange={handleDataChange}>
            <option value>
              Crédito Suplementar
            </option>
          </select>
        </div>
        <div className='d-flex mb-2' style={{ height: '70px' }}>
          <label className='input-group-text'>
            Tipo de Relatório:
          </label>
          <select className='form-select' value={reportType} onChange={handleReportTypeChange}>
            <option value='geral'>Geral</option>
            <option value='anual'>Anual</option>
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