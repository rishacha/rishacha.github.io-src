module.exports = {
    head: [
        ['link', { rel: 'stylesheet', href: 'https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.5.1/katex.min.css' }]
    ],
    title: 'Rishabh\'s Blog',
    description: 'Just playing around',
    themeConfig: {
        nav: [
            {
                text: 'Sections',
                items: [
                    { text: 'Data Science', link: '/ds/' },
                    { text: 'Coding', link: '/coding/' }
                ]
            },
            {
                text:'Projects',
                link:'/'
            }
        ],
        // sidebar:auto,
        sidebar: {
            '/ds/':[
                '',
                'svm'
            ],
            '/coding/':[
                '',
                'tensorflow'
            ],
            '/': [
                '/',
                'contact',
                'about'
            ]
        }

    },
    markdown: {
        // options for markdown-it-anchor
        // anchor: { permalink: false },
        config: md => {
            md.use(require("markdown-it-katex"));
        }
    },


}