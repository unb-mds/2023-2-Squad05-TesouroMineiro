import React from 'react';
import Chart from 'react-apexcharts'

const Graficos = () => {
    let dataExample = {
        options: {
            chart: {
                id: 'example'
            },
            xaxis: {
                //Deve ser alterado pelas categorias dos dados dos DOU
                categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
            }
        },
        series: [{
            name: 'series-1',
            //Deve ser alterado pelos dados obtidos do dou
            data: [30, 40, 35, 50, 49, 60, 70, 91, 125]
        }]
    }

    return (
        <Chart options={dataExample.options} series={dataExample.series} type="bar" width={500} height={320}></Chart>
    )
}

export default Graficos;