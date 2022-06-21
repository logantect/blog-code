package io.devdog.springtransaction.service;

import io.devdog.springtransaction.domain.Post;
import io.devdog.springtransaction.domain.PostRepository;
import io.devdog.springtransaction.service.PostCommand.UpdatePost;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Slf4j
@RequiredArgsConstructor
@Service
public class PostService {

  private final PostRepository postRepository;

  public Long registerPost(PostCommand.RegisterPost command) {
    Post savedPost = postRepository.save(command.toEntity());
    return savedPost.getId();
  }

  public Post getPost(final Long postId) {
    return postRepository.findById(postId).orElseThrow();
  }

  public void updateNoTransactional(final Long postId, PostCommand.UpdatePost command) {
    updatePost(postId, command);
  }

  @Transactional
  void updatePost(final Long postId, UpdatePost command) {
    Post post = postRepository.findById(postId).orElseThrow();
    post.changeContent(command.getContent()); // Not Dirty Checking
  }


}