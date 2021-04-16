<template>
  <div id="app">
   <el-tabs v-model="activeName" @tab-click="handleClick">
    <el-tab-pane label="字幕文件" name="first">
      <el-tabs tab-position="left" style="height: 200px;">
        <el-tab-pane label="网易见外">
         <el-link  type="success" href="https://jianwai.youdao.com/" target="_blank">网易见外</el-link>
        </el-tab-pane>
        <el-tab-pane label="pytranscriber">pytranscriber</el-tab-pane>
        <el-tab-pane label="百度语音识别">百度语音识别</el-tab-pane>
        <el-tab-pane label="文档">
        <el-link  type="success" href="https://github.com/raryelcostasouza/pyTranscriber" target="_blank">pyTranscriber</el-link>
        </el-tab-pane>
      </el-tabs>
    </el-tab-pane>
    <el-tab-pane label="关键词提取" name="second">
      <el-tabs tab-position="left" style="height: 200px;">
        <el-tab-pane label="TF-IDF">
        TF-IDF ：用于反映一个词对于某篇文档的重要性。过滤掉常见的词语，保留重要的词语 

        如果某个词在一篇文档中出现的频率高，则TF 高；并且在其他文档中很少出现，则 IDF 高，TF-IDF 就是将二者相乘为 TF * IDF， 这样这个词具有很好的类别区分能力。 

        在  jieba 用以下代码实现 

          jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=()) 
          <el-input
            type="textarea"
            :rows="2"
            placeholder="请输入内容"
            v-model="textarea" style="width:90%;">
          </el-input>
          <el-button type="success" style="width:10%;" @click="getTags()">关键词提取</el-button>
          <div v-for="tag in tags" :key="tag">
            <el-radio v-model="checkedTag" :label="tag" border> {{ tag }} </el-radio>
          </div>
        </el-tab-pane>
        <el-tab-pane label="TextRank"> 由 PageRank 改进而来，将文本中的词看作图中的节点，通过边相互连接，权重高的节点作为关键词。 

   在  jieba 用以下代码实现 

    jieba.analyse.textrank(sentence, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v')) </el-tab-pane>
        <el-tab-pane label=" LDA "> 一般步骤为：文件加载 -> jieba 分词 -> 去停用词 -> 构建词袋模型 -> LDA 模型训练 -> 结果可视化。</el-tab-pane>
        <el-tab-pane label=" pyhanlp  ">可以用 HanLP 的 TextRankKeyword 实现 

    from pyhanlp import *
    result = HanLP.extractKeyword(sentence, 20)
    print(result)

      </el-tab-pane>
        <el-tab-pane label="文档">
        <el-link  type="success" href="https://cloud.tencent.com/developer/article/1388397" target="_blank">NLP参考文档</el-link>
        <br>
        <el-link  type="success" href="https://github.com/fxsjy/jieba" target="_blank">jieba</el-link>
        </el-tab-pane>
      </el-tabs>
    </el-tab-pane>
    <el-tab-pane label="生成表情" name="third">
      <el-tabs tab-position="left" style="height: 200px;">
        <el-tab-pane label="搜狗表情">
         <el-link  type="success" href="https://pic.sogou.com/pic/emo/" target="_blank">搜狗表情</el-link>
        </el-tab-pane>
        <el-tab-pane label="斗图啦">
          <el-link  type="success" href="https://www.doutula.com" target="_blank">斗图啦</el-link>
        </el-tab-pane>
        <el-tab-pane label="斗图终结者">
          <el-link  type="success" href="https://www.52doutu.cn" target="_blank">斗图终结者</el-link>
        </el-tab-pane>
        <el-tab-pane label="逗比拯救世界">
          <el-link  type="success" href="http://www.bee-ji.com" target="_blank">逗比拯救世界</el-link>
        </el-tab-pane>
        <el-tab-pane label="文档">
        <el-link  type="success" href="https://github.com/QiaoJianCheng/Gifin" target="_blank">斗图</el-link>
        </el-tab-pane>
      </el-tabs>
    </el-tab-pane>
    <el-tab-pane label="字幕样式" name="fourth">字幕样式</el-tab-pane>
  </el-tabs>
  </div>
</template>

<script>
const url = "http://127.0.0.1:5000/api";
export default {
   data() {
      return {
        activeName: 'second',
        textarea: '',
        tags: []
      };
    },
    methods: {
      handleClick(tab, event) {
        console.log(tab, event);
      },
      getTags() {
       this.$axios.get(url + '/TFIDF/' + this.textarea)
          .then(resp => {
            this.tags=resp.data
            console.log(resp);
          }).catch(err => {
            console.log(err);
          })

      }
    }
}
</script>

<style>
#app {
  font-family: Helvetica, sans-serif;
}
 .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    width: 480px;
  }
</style>
