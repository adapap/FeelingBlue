<template lang='pug'>
    v-app#app
        v-app-bar.white--text(app color='primary')
            v-toolbar-title FeelingBlue?
        v-content.pb-4
            v-container.px-0(fluid)
                v-row(justify='center' ): v-col.mx-2.text-center(offset='2' cols='8'): v-card.pa-2 
                    v-container.px(fluid)
                        v-row.text-center(justify='center' no-gutters)
                            .display-1.mt-2.font-weight-bold FeelingBlue: A Sentiment Analysis of JetBlue
                        v-row(justify='center' no-gutters)
                            v-col.mx-2.text-left(cols='10' offset='1')
                                .mt-2.body-1.
                                    All airline companies face the same set of issues in the industry, including unexpected delays and cancellations.
                                    If JetBlue looks beyond industry-wide pain-points, then the company can pinpoint internal weaknesses and address
                                    them using their strength. Our analysis focused on providing a unique perspective on keeping customers happy.
                                .mt-2.title Over 5000 unique customer data points analyzed
                                .body-1.
                                    FeelingBlue uses data scraping techniques to collect customer feedback from several online media sources, including Twitter, Reddit, TripAdvisor, AirlineQuality, and Kayak.
                                .mt-2.title Focus on subjects, not subjectivity
                                .body-1.
                                    Our approach took advantage of the power of natural language processing in order to perform a rule-based sentiment analysis.
                                    We measured the polarity of the data we found in order to approximate a sentiment, weighing those which
                                    were objective more heavily than those which were subjective. Our approach also cleaned and prepared the data
                                    in order to make it easier for learning models to train on.
                v-row.mt-12(justify='center' no-gutters)
                    v-card.pa-6(color='primary' elevation='8'): v-container: v-row
                        Pie(sentiment='positive')
                        v-spacer
                        Pie(sentiment='negative')
                v-row.my-4(justify='center' align='center' no-gutters)
                    v-col.mx-4(cols='2'): v-img(src='./assets/twitter.png')
                    v-col.mx-4(cols='2'): v-img(src='./assets/kayak.png')
                    v-col.mx-4(cols='2'): v-img(src='./assets/tripadvisor.png')
                    v-col.mx-4(cols='2'): v-img(src='./assets/reddit.png')
                    v-col.mx-4(cols='2'): v-img(src='./assets/consumeraffairs.png')
                v-row(justify='center' no-gutters): v-col(cols='8'): v-card.pa-3
                    v-card-title.display-2 The Pain Points
                    .body-1.px-3
                        | FeelingBlue found that overall, 
                        b majority 
                        | of customer feedback is of 
                        b positive sentiment. 
                        | The percentage of customers who gave positive feedback was higher than those who gave the opposite. 
                        b 44% 
                        | of feedback categories was determined to be more 
                        b positive 
                        | while 
                        b 33% 
                        | of feedback categories favored a 
                        b negative sentiment. 
                        | The 3 categories with a more negative sentiment included 
                        b Delayed Flights, Cancellations, and Accessibility. 
                        | Problems concerning these three topics evoked the most negative response from customers. 
                        | Many feel that the way the airline handles Delayed Flights and cancellations could be improved. 
                        | It is also evident that more measures could be made to make JetBlue airlines more accessible to customers with disabilities such as wheelchairs.
                    v-card-text "JetBlue terminal in LAX does not have a family bathroom. I'm in a wheelchair and they had to clear out the whole ladies' room so my husband could help me. If you have a young children, you have to take them with you or leave them on their own."
                v-row.my-5(justify='center' no-gutters): v-col(cols='8'): v-card.pa-2
                    .body-1.px-2
                    v-card-title.display-2
                        | How to keep the
                        b #FleetOnFleek
                    v-card-text "Tough choices, but I did all simultaneously as a business traveler. Best experience in a long time! #wishmyflightwaslonger #what"
</template>

<script>
import Pie from './Pie.vue'
export default {
    name: 'App',
    components: {
        Pie,
    },
}
</script>

<style scoped>
.v-content {
    background: url('assets/background.png');
}
</style>