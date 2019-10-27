<script>
import { Pie } from 'vue-chartjs'
import parsed from './data/parsed.json'

export default {
    extends: Pie,
    props: {
        sentiment: String
    },
    data() {
        var total = parsed['total']
        var keys = Object.keys(parsed).filter(x => x != 'total')
        var keyName = {
            'info': 'Information',
            'tech': 'Technology',
            'business': 'Business Operations & Pricing',
            'staff': 'Staff & Service',
            'luggage': 'Luggage & Carry-ons',
            'experience': 'Consumer Experience',
            'delay': 'Delayed Flights',
            'cancel': 'Cancellations & Rescheduling',
            'accessibility': 'Accessibility',
        }
        return {
            rawData: {
            labels: keys.map(x => keyName[x]),
            datasets: [
                {
                    backgroundColor: [
                        '#FF5252',
                        '#4CAF50',
                        '#FF9800',
                        '#03A9F4',
                        '#CDDC39',
                        '#FFEB3B',
                        '#9C27B0',
                        '#E91E63',
                        '#3F51B5',
                    ],
                    borderWidth: 2,
                    data: keys.map(x => Math.round(parsed[x][this.sentiment] / total[this.sentiment] * 100, 2))
                }
            ]
        },
        options: {
            title: {
                display: true,
                fontColor: 'white',
                fontSize: 28,
                text: this.sentiment == 'positive' ? 'Positive Results' : 'Negative Results',
            },
            legend: {
                display: false,
            },
            tooltips: {
                callbacks: {
                    label: function(t, data) {
                        return `${data.labels[t.index]}: ${data.datasets[0].data[t.index]}%`
                    }
                }
            }
        }
      }
    },
    mounted () {
      this.renderChart(this.rawData, this.options)
    }
  }
</script>