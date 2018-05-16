// console.log(__dirname);
module.exports = {
    // configureWebpack: {
    //     resolve: {
    //       alias: {
    //         '@alias': __dirname+'/assets/svm'
    //       }
    //     }
    //   },
    head: [
        ['link', { rel: 'stylesheet', href: 'https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.5.1/katex.min.css' }]
    ],

    title: 'Hello VuePress',
    description: 'Just playing around',
themeConfig:{
    sidebar:[
        {
            title: 'Group 1',
            collapsable: false,
            children: [
              '/',
              ['svm','SVM']
            ]
          },
        ],
    },
    markdown: {
        // options for markdown-it-anchor
        // anchor: { permalink: false },
        config: md => {
            md.use(require("markdown-it-katex"));
        }
    },


}