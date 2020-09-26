const axios = require("axios");
const cheerio = require("cheerio");
const log = console.log;

const getHtml = async () => {
  try {
    return await axios.get("https://github.com/1-EXON/DarkAlgo");
  } catch (error) {
    console.error(error);
  }
};

getHtml()
  .then(html => {
    let ulList = [];
    const $ = cheerio.load(html.data);
    const $bodyList = $("#js-repo-pjax-container > div.container-xl.clearfix.new-discussion-timeline.px-3.px-md-4.px-lg-5 > div > div.gutter-condensed.gutter-lg.flex-column.flex-md-row.d-flex > div.flex-shrink-0.col-12.col-md-9.mb-4.mb-md-0").children("#readme > div.Box-body.px-5.pb-5");

    $bodyList.each(function(i, elem) {
      ulList[i] = {
          title: $(this).find('article > h1').text(),
      };
    });

    return ulList;
  })
  .then(res => log(res));