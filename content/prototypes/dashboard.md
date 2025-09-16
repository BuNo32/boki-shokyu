# 学習ダッシュボード（見本）

以下は**localStorage**に保存されたスコアから、章ごとの進捗を集計したものです。

<div id="dashboard"></div>

<script>
  // 外部スクリプト（dashboard.js）が読まれた後に実行されるように調整
  (function runWhenReady(cb){
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', cb, { once: true });
    } else {
      setTimeout(cb, 0);
    }
  })(function(){
    // protos配下から quizzes へは 1 階層上
    if (typeof renderDashboard === 'function') {
      renderDashboard('../quizzes/index.json','dashboard');
    } else {
      console.warn('renderDashboard is not available yet');
    }
  });
</script>
