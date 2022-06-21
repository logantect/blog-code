package io.devdog.springtransaction.service;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

import io.devdog.springtransaction.domain.Post;
import io.devdog.springtransaction.domain.PostRepository;
import io.devdog.springtransaction.service.PostCommand.RegisterPost;
import io.devdog.springtransaction.service.PostCommand.UpdatePost;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit.jupiter.SpringExtension;

@ExtendWith(SpringExtension.class)
@SpringBootTest
class PostServiceTest {

  @Autowired
  private PostService postService;

  @Test
  @DisplayName("@Transactional 없는 메서드 통해서 업데이트 - 트랜잭션 적용 안됨")
  void updateNoTransactional() {
    Long postId = postService.registerPost(new RegisterPost("제목", "내용"));
    postService.updateNoTransactional(postId, new UpdatePost("제목", "내용수정"));
    Post updatedPost = postService.getPost(postId);
    assertThat(updatedPost.getContent()).isEqualTo("내용");
  }
}